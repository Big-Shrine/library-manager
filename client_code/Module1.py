import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import mysql.connector as mys
cobj=mys.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
curob=cobj.cursor()

# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
def executor(h):
  curob.execute(h)
  cobj.commit()
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
        self.label_6.visible = True
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
    self.label_5.visible = True
    