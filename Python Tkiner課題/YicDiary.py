from cProfile import label
from doctest import master
import tkinter as tk
import tkinter.ttk as ttk
import datetime as da
import calendar as ca
import pymysql.cursors
import imp
import tkinter
import pymysql.cursors


WEEK = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLOUR = ['red', 'black', 'black', 'black','black', 'black', 'blue']
actions = ('学校','試験', '課題', '行事', '就活', 'アルバイト','旅行')

class MainAppli():
    '''アプリ本体'''

    def __init__(self, master):
        master.title('ログイン画面')
        master.geometry('520x280')
        master.resizable(0, 0)
        master.grid_columnconfigure((0, 2), weight=2)

        self.master = master
        self.widgets = []
        self.create_widgets()
        
    def create_widgets(self):

            self.name_label = tkinter.Label(self.master, text="ユーザー名") 
            self.name_label.grid(row=0, column=0)
            self.widgets.append(self.name_label)

            self.name_entry = tkinter.Entry(self.master)
            self.name_entry.grid(row=0,column=1)
            self.widgets.append(self.name_entry)

            #パスワード入力用ウィジェット
            self.pass_label = tkinter.Label(self.master,text = "パスワード")
            self.pass_label.grid(row=1, column=0)
            self.widgets.append(self.pass_label)    
                
            self.pass_entry = tkinter.Entry(self.master, show="*" )
            self.pass_entry.grid(row=1, column=1)
            self.widgets.append(self.pass_entry)

            #ログインボタン
            self.login_button = tkinter.Button(self.master, text="ログイン", command=self.login)
            self.login_button.grid(row=2, column=0, columnspan=3,)
            self.widgets.append(self.login_button)


            #登録ボタン
            self.register_button = tkinter.Button(self.master, text="登録", command=self.register)
            self.register_button.grid(row=3, column=0, columnspan=3,)
            self.widgets.append(self.register_button)

            #ウィジェットすべてを中央寄せ
            self.master.grid_anchor(tkinter.CENTER)

    def login(self):
        get_username = self.name_entry.get()
        get_password = self.pass_entry.get()

        # データベースに予定の問い合わせを行う
        connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='',
                                db='apr01',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

        try:
            connection.begin()
            with connection.cursor() as cursor:

                cursor = connection.cursor()
                print("select memo　を実行")
                sql1 = "select user_name, user_password from user_table"
                cursor.execute(sql1)
                results1 = cursor.fetchall()

                sql2 = "select user_ID from user_table"
                cursor.execute(sql2)
                results2 = cursor.fetchall()

                print(results1)
               #print(len(results))
      
                if len(get_username) == 0:
                   self.error_pass()

                elif len(get_password) == 0:
                   self.error_pass()

                for i in range(len(results1)):
                   if results1[i]["user_name"] == get_username:
                       if results1[i]["user_password"] == get_password:
                           next_userID = results2[i]["user_ID"] 
                           self.widget_destory()
                       

                           YicDiary(self.master, next_userID, get_username)
                           self.master.mainloop()

                self.error_pass()

        except Exception as e:
            print('error:', e)
            connection.rollback()
        
         
        connection.close()


    def widget_destory(self):
        for widget in self.widgets:
            widget.destory()

    def error_pass(self):
        pass

    def register(self):
        pass

        # ログイン完了していないのでウィジェットは作成しない

    def start(self, login_name):
        '''アプリを起動する'''

        # ログインユーザー名を表示する
        self.message = tkinter.Label(
            self.master,
            font=("",40),
            text=login_name + "でログイン中"
        )
        self.message.pack()

        # 必要に応じてウィジェット作成やイベントの設定なども行う

class YicDiary:
  def __init__(self, master, next_userID, get_username):
    
    self.sub_win = None

    self.year  = da.date.today().year
    self.mon = da.date.today().month
    self.today = da.date.today().day

    self.title = None
    # 左側のカレンダー部分
    leftFrame = tk.Frame(root)
    leftFrame.grid(row=0, column=0)
    self.leftBuild(leftFrame)

    # 右側の予定管理部分
    rightFrame = tk.Frame(root)
    rightFrame.grid(row=0, column=1)
    self.rightBuild(rightFrame)


  #-----------------------------------------------------------------
  # アプリの左側の領域を作成する
  #
  # leftFrame: 左側のフレーム
  def leftBuild(self, leftFrame):
    self.viewLabel = tk.Label(leftFrame, font=('', 10))
    beforButton = tk.Button(leftFrame, text='＜', font=('', 10), command=lambda:self.disp(-1))
    nextButton = tk.Button(leftFrame, text='＞', font=('', 10), command=lambda:self.disp(1))

    self.viewLabel.grid(row=0, column=1, pady=10, padx=10)
    beforButton.grid(row=0, column=0, pady=10, padx=10)
    nextButton.grid(row=0, column=2, pady=10, padx=10)

    self.calendar = tk.Frame(leftFrame)
    self.calendar.grid(row=1, column=0, columnspan=3)
    self.disp(0)


  #-----------------------------------------------------------------
  # アプリの右側の領域を作成する
  #
  # rightFrame: 右側のフレーム
  def rightBuild(self, rightFrame):
    r1_frame = tk.Frame(rightFrame)
    r1_frame.grid(row=0, column=0, pady=10)

    temp = '{}年{}月{}日の予定'.format(self.year, self.mon, self.today)
    self.title = tk.Label(r1_frame, text=temp, font=('', 12))
    self.title.grid(row=0, column=0, padx=20)

    button = tk.Button(rightFrame, text='追加', command=lambda:self.add())
    button.grid(row=0, column=1)

    self.r2_frame = tk.Frame(rightFrame)
    self.r2_frame.grid(row=1, column=0)

    self.schedule()


  #-----------------------------------------------------------------
  # アプリの右側の領域に予定を表示する
  #
  def schedule(self):
    # ウィジットを廃棄
    for widget in self.r2_frame.winfo_children():
      widget.destroy()

    # データベースに予定の問い合わせを行う
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='',
                                db='apr01',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
      connection.begin()
      with connection.cursor() as cursor:
        cursor = connection.cursor()
        print("select memo　を実行")
        sql = "select Memo from plan_table Where Plan_date = '{}-{}-{}';".format(self.year, self.mon, self.today)
    
        cursor.execute(sql)

        results = cursor.fetchall()
        print(results)
        #print(len(results))

        for i, row in enumerate(results):
          x = row["Memo"]
          label = tk.Label(self.r2_frame, text=x, font=('',12))
          label.grid(row=i,column=0)
        connection.commit()
      
        


    except Exception as e:
      print('error:',e)
      connection.rollback()
    
    finally:
      connection.close()


  #-----------------------------------------------------------------
  # カレンダーを表示する
  #
  # argv: -1 = 前月
  #        0 = 今月（起動時のみ）
  #        1 = 次月
  def disp(self, argv):
    self.mon = self.mon + argv
    if self.mon < 1:
      self.mon, self.year = 12, self.year - 1
    elif self.mon > 12:
      self.mon, self.year = 1, self.year + 1

    self.viewLabel['text'] = '{}年{}月'.format(self.year, self.mon)

    cal = ca.Calendar(firstweekday=6)
    cal = cal.monthdayscalendar(self.year, self.mon)

    # ウィジットを廃棄
    for widget in self.calendar.winfo_children():
      widget.destroy()

    # 見出し行
    r = 0
    for i, x in enumerate(WEEK):
      label_day = tk.Label(self.calendar, text=x, font=('', 10), width=3, fg=WEEK_COLOUR[i])
      label_day.grid(row=r, column=i, pady=1)

    # カレンダー本体
    r = 1
    for week in cal:
      for i, day in enumerate(week):
        if day == 0: day = ' ' 
        label_day = tk.Label(self.calendar, text=day, font=('', 10), fg=WEEK_COLOUR[i], borderwidth=1)
        if (da.date.today().year, da.date.today().month, da.date.today().day) == (self.year, self.mon, day):
          label_day['relief'] = 'solid'
        label_day.bind('<Button-1>', self.click)
        label_day.grid(row=r, column=i, padx=2, pady=1)
      r = r + 1

    # 画面右側の表示を変更
    if self.title is not None:
      self.today = 1
      self.title['text'] = '{}年{}月{}日の予定'.format(self.year, self.mon, self.today)


  #-----------------------------------------------------------------
  # 予定を追加したときに呼び出されるメソッド
  #
  def add(self):
    if self.sub_win == None or not self.sub_win.winfo_exists():
      self.sub_win = tk.Toplevel()
      self.sub_win.geometry("300x300")
      self.sub_win.resizable(0, 0)

      # ラベル
      sb1_frame = tk.Frame(self.sub_win)
      sb1_frame.grid(row=0, column=0)
      temp = '{}年{}月{}日　追加する予定'.format(self.year, self.mon, self.today)
      title = tk.Label(sb1_frame, text=temp, font=('', 12))
      title.grid(row=0, column=0)

      # 予定種別（コンボボックス）
      sb2_frame = tk.Frame(self.sub_win)
      sb2_frame.grid(row=1, column=0)
      label_1 = tk.Label(sb2_frame, text='種別 : 　', font=('', 10))
      label_1.grid(row=0, column=0, sticky=tk.W)
      self.combo = ttk.Combobox(sb2_frame, state='readonly', values=actions)
      self.combo.current(0)
      self.combo.grid(row=0, column=1)

      # テキストエリア（垂直スクロール付）
      sb3_frame = tk.Frame(self.sub_win)
      sb3_frame.grid(row=2, column=0)
      self.text = tk.Text(sb3_frame, width=40, height=15)
      self.text.grid(row=0, column=0)
      scroll_v = tk.Scrollbar(sb3_frame, orient=tk.VERTICAL, command=self.text.yview)
      scroll_v.grid(row=0, column=1, sticky=tk.N+tk.S)
      self.text["yscrollcommand"] = scroll_v.set

      # 保存ボタン
      sb4_frame = tk.Frame(self.sub_win)
      sb4_frame.grid(row=3, column=0, sticky=tk.NE)
      button = tk.Button(sb4_frame, text='保存', command=lambda:self.done())
      button.pack(padx=10, pady=10)
    elif self.sub_win != None and self.sub_win.winfo_exists():
      self.sub_win.lift()


  def get_kinds_ID(self,kinds):
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='',
                                db='apri01',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
      # トランザクション開始
      connection.begin()
      with connection.cursor() as cursor:
        cursor = connection.cursor()

        sql = 'select plan_type_ID from plan_type_table WHERE Plan_type = "{}";'.format(kinds)
        cursor.execute(sql)

        results = cursor.fetchone()
        #print(results)
        return results["plan_type_ID"]

      connection.commit()


    except:
      print('error')
    
    finally:
      connection.close()



  #-----------------------------------------------------------------
  # 予定追加ウィンドウで「保存」を押したときに呼び出されるメソッド
  #
  def done(self):
    # データベースに新規予定を挿入する
    # 日付
    days = '{}-{}-{}'.format(self.year, self.mon, self.today)
    print(days)

    # 種別
    kinds = self.combo.get()
    self.combo.get()
    print(kinds)

    # 種別IDを取得
    kinds_ID = self.get_kinds_ID(kinds)
    #self.get_kinds_ID(kinds)
    print(kinds_ID)

    # 予定
    memo =self.text.get("1.0","end")
    print(memo)

    #　データベースに挿入する
    connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='apri01',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    try:
      # トランザクション開始
      connection.begin()
      with connection.cursor() as cursor:
        cursor = connection.cursor()

        sql = 'INSERT INTO plan_table(Plan_date,Plan_type_ID,Memo) VALUES("{}",{},"{}");'.format(days,kinds_ID,memo)
        cursor.execute(sql)

        #results = cursor.fetchall()
        #print(results)

      connection.commit()


    except:
      print('error')
    
    finally:
      connection.close()


    self.sub_win.destroy()


  #-----------------------------------------------------------------
  # 日付をクリックした際に呼びだされるメソッド（コールバック関数）
  #
  # event: 左クリックイベント <Button-1>
  def click(self, event):
    day = event.widget['text']
    if day != ' ':
      self.title['text'] = '{}年{}月{}日の予定'.format(self.year, self.mon, day)
      self.today = day
    self.schedule()

def Main():

  master = tk.Tk()
  MainAppli(master)
  master.mainloop()

if __name__ == '__main__':
  Main()
