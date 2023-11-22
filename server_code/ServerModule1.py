import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pymysql.cursors as mys
cobj=mys.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
curob=cobj.cursor()

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

def executor(h):
  curob.execute(h)
  cobj.commit()
@anvil.server.callable
def issueBooks():
  customer=self.customer.text
  bookid=self.bookid.text
  curob.execute("select BOOK_ID, NAME, COPIES, STATUS from books")
  books=curob.fetchall()
  flag=False
  for i in books:
    if bookid in i:
      flag=True
      l=i[2]-1
      if l==0:
        status=f"update books set COPIES={str(l)}, STATUS=0 where BOOK_ID={i[0]}"
        executor(status)
      elif l==-1:
        alert('Book unavailable')
        continue
      else:
        status=f"update books set COPIES={str(l)} where BOOK_ID={i[0]}"
        executor(status)
      datetime=self.datetime.text
      if datetime:
        c=f"Insert into book_issues(customer_id, book_id, date_of_issue) values({customer},{bookid},'{datetime}')"
      else:
        c=f"Insert into book_issues(customer_id, book_id) values({customer},{bookid})"
      executor(c)
      curob.execute("select customer_id,books_issued from customer_details")
      h=curob.fetchall()
      for i in h:
        if customer in i:
          issued=f"update customer_details set books_issued={str(i[1]+1)} where customer_id={i[0]}"
          executor(issued)
      break
  if not flag:
    alert('The entered Customer ID or Book ID is invalid')

@anvil.server.callable
def addBook():
   bkid=self.bookid2.text
   gre=self.genre.text
   bkname=self.bookname.text
   auth=self.author.text
   copies=int(self.copies.text)
   if copies!=0:
     status=1
   else:
     status=0
   st="Insert into books values('{}','{}','{}','{}',{},{})".format(bkid,gre,bkname,auth,copies,status)
   executor(st) 