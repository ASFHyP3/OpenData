FROM amazon/aws-cli

COPY .aws/ /root/.aws/
COPY docker-entrypoint.sh /root/

ENTRYPOINT ["/root/docker-entrypoint.sh"]