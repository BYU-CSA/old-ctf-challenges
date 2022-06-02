FROM mikee314/tcpserver

EXPOSE 9000

USER tcpbroker

WORKDIR /home/tcpbroker

COPY flag.txt /home/tcpbroker/flag.txt
COPY small.txt /home/tcpbroker/small.txt
COPY large.txt /home/tcpbroker/large.txt
COPY wordle /home/tcpbroker/wordle

CMD ["tcpserver", "0.0.0.0", "9000", "/home/tcpbroker/wordle"]

