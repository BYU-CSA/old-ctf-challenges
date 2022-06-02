# Too Many Times
Level: Hard

Description:
```
My enemy was sending secret messages to his allies with a supposedly "unbreakable" cipher, but I think he made a mistake.

Message 1 - `LKAHEIIWPQPGQCUOXHIQFIUBXEHJBRU`

Message 2 - `RQXJTVSYVJVDJPASBLDQGIWWHPWISKT`

Message 3 - `DTKXPPECBFVHWLIEQXDNCFWCIYPXYFB`
```

## Writeup
Breaking this encryption relies on multiple messages being encrypted using a one time pad with the same secret key. 

* Secret key - `kmgfldakjfpdsoamxspwoeriqwpeqro`
* Message 1 - `byuctfimgladyoucapturedthisflag`
* Message 2 - `hereissomegarbagetouseforthectf`
* Message 3 - `thesemessageexistforobfuscation`


**Flag** - `byuctf{imgladyoucapturedthisflag}`