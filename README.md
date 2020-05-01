# CalcCo
This is a Simple Calculator consisiting of two main functions: 
1.  One is of Calculation of addition, subtraction, multiplication and division of two numbers (They are named as var_1 and var_2). This calculation can accept both whole numbers and decimals.
2.  The other is a Factorial of a single number (Named as var_1). This function can only calculate factorial of integer values, which means it can not accept decimal numbers for computation.

Testing process:
1.You will need to use an API client e.g. Postman to run the URL's and receive values for the Calculator. 
2.Download the postman application into your local machine
3.The API end points sends values through the "POST" method. Make sure this is selected!
4.Enter the URL for each function as below:

  a)Addition: http://127.0.0.1:5000/Add, Enter var_1 and var_2 as keys and enter corresponding values such as 1, 2. Expected       result {status:200, result:3.0}
  b)Subtraction: http://127.0.0.1:5000/Subtract, Enter var_1 and var_2 as keys and enter corresponding values such as 2, 3. Expected result {status:200, result:-1.0}
  c)Multiplication: http://127.0.0.1:5000/Multiply, Enter var_1 and var_2 as keys and enter corresponding values such as 2, 3. {status:200, result:6.0}
  d)Division: http://127.0.0.1:5000/Divide, Enter var_1 and var_2 as keys and enter corresponding values such as 6, 3. {status:200, result:2.0}
  e)Factorial: http://127.0.0.1:5000/Factorial , enter var_1 as key, and enter a value say 3. Expected result {status:200, result:6}
  
Note: Set the Query Params (that is the values you would like worked on by the function) in the table below. Key column is var_1 and var_2 for Calculation and var_1 only for the factorial. Value are the values you would like to be worked on by the corresponding functions.

5.Then click on Send.
6. Result of the computation are dispalyed in the table below.



