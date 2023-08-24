# On The Job Series
## On The Job 1:
1. What language was this malware written in?
```
byuctf{bash}
```
## On The Job 2:
2. What is the Domain that the malware was interacting with?
```
byuctf{domain.io}
```
## On The Job 3:
3. Who is the group responsible?

flag format: byuctf{GXXXX-NAME} (mitre group number+NAME)
```
byuctf{G0105-DarkVishnya}
```
## On The Job 4:
4. What MITRE Technique listed could be used to deliver this malware? Look at the malware specifically for hints.

flag format: byuctf{TXXXX}
```
- byuctf{T1200}
```
## On The Job 5:
5. What MITRE Attack Techniques were present within the Malware?

flag format: byuctf{TXXXX,TXXXX,TXXXX,TXXXX,TXXXX} (from lowest to highest)
```
byuctf{T1040,T1046,T1135,T1571,T1588}
```
- byuctf{T1588.002}
## On the Job 6:
6. What Sub-technique was used, specifcally relating to three tools:

flag format: byuctf{TXXXX.XXX}
```
byuctf{T1588.002}
```