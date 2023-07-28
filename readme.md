## Steps to Run 🏃‍♀️ 

1. restructure the project to seperate frontend from app as per above project
2. run below command  

~~~bash  
  nuitka --module --report=REPORT.txt --show-modules --verbose --show-memory --show-progress --include-plugin-directory=app --output-dir=out app
~~~

NOTE: It doesnt support blueprint as of now.