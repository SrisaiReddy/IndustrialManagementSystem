# importing module 
import cx_Oracle 


# Create a table in Oracle database 
try: 

	con = cx_Oracle.connect('SSAGRO/SSAGRO') 
	
	# Now execute the sqlquery 				
	cursor = con.cursor() 
	uname="PAVAN"
	passw="123"
	
	# Creating a table srollno heading which is number 
	#cursor.execute("select * from SS_USER_ACCESS where USER_ID = '"+uname+"'")
	#cursor.execute("insert into SS_USER_ACCESS(USER_ID,PASS) values('"+uname+"','"+passw+"')")
	#cursor.execute("update SS_USER_ACCESS set PASS = '"+passw+"' where USER_ID = '"+uname+"'")
	#con.commit()
	#raw=cursor.fetchall()

	#for i in raw:
	#	print(i)

except cx_Oracle.DatabaseError as e: 
	print("There is a problem with Oracle", e) 

# by writing finally if any error occurs 
# then also we can close the all database operation 
finally: 
 	if cursor: 
 		cursor.close()
 	if con: 
 		con.close() 

print("Cursor closed")
