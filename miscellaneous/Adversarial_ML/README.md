## Adversarial ML
Level - Medium

Author: Justin Giboney

Description:
```
Visit http://giboney2.byu.edu:5000. Read the instructions. Get the flag. You have to be on campus to get to the server (or VPN).
```

**Flag** - byuctf{y0u_g0t_my_d1n0s4ur}

## Writeup 
One possible way to do this is to submit the following queries:

1. None : No query submitted.

2. safe : select * from customers where FirstName = 'nancy'

3. safe : select * from customers where FirstName = 'nancy'

4. safe : select * from customers where FirstName = 'nancy'

5. safe : select * from customers where FirstName = 'nancy'

6. Bad query. Try again.no such column: LirstName : select * from customers where LirstName = 'edwards'

7. Bad query. Try again.no such column: LirstName : select * from customers where LirstName = 'edwards'

8. Bad query. Try again.no such column: LirstName : select * from customers where LirstName = 'edwards'

9. safe : select * from customers where LastName = 'edwards'

10. safe : select * from customers where LastName = 'edwards'

11. safe : select * from customers where LastName = 'edwards'

12. safe : select * from customers where LastName = 'edwards'

13. safe : select * from employees where firstname = 'Jack'

14. safe : select * from employees where firstname = 'Jack'

15. safe : select * from employees where firstname = 'Jack'

16. malicious : select * from employees

17. malicious : select * from employees where firstname = 'Nancy'

18. malicious : select * from employees where LastName = 'Edwards'

19. malicious : select '1958-12-08'

20. malicious : select * from employees
