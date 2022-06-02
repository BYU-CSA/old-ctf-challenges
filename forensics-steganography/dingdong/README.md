# Ding Dong
Level: Medium

Description:
```
Here is a packet capture of Ian while on campus one afternoon. Can you figure out what he was doing?


1. What is Ian's IP and MAC address? (flag format `byuctf{10.10.10.10_11:22:33:44:55:66}`)
2. How many different DNS queries of type A were made? (flag format `byuctf{0000}`)
3. How many packets have the `ACK` flag enabled? (flag format `byuctf{0000}`)
4. What is the version number for the Linux server that sent a packet with `redsonic` as the user agent? (flag format `byuctf{1.1.1}`)
5. What are the two IPs that function as DNS servers? (flag format `byuctf{10.10.10.10_11.11.11.11}`)
6. What is the hidden flag?
```

## Writeup
1. What is Ian's IP and MAC address?
    - `byuctf{10.37.131.2_58:96:1d:95:29:41}`
1. How many different DNS queries of type A were made?
    - `byuctf{36}`
1. How many packets have the ACK flag enabled?
    - `byuctf{1509}`
1. What is the version number for the Linux server that sent a packet with redsonic as the user agent?
    - `byuctf{4.9.125}`
1. What are the two IPs that function as DNS servers?
    - `byuctf{10.8.0.2_10.8.0.8}` or `byuctf{10.8.0.8_10.8.0.2}`
1. What is the hidden flag?
    - `byuctf{p1ngp0ngers1zc00l}`