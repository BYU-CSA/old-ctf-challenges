FROM nsjailcontainer

WORKDIR /jail

COPY ./jail .

RUN chmod -R 755 .

CMD nsjail -Ml --port 9000 --disable_proc --chroot /jail --tmpfsmount /home/qr -- /bin/generator
