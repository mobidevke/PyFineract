#!/bin/bash

if [[ -f /certs/key.p12 ]];
then
   echo "Cert file found. Importing..."
   keytool -importkeystore -noprompt -srckeystore /certs/key.p12 -srcstorepass changeit -srcstoretype PKCS12 -destkeystore /usr/share/tomcat.keystore -deststoretype JKS -deststorepass password -destkeypass password
else
   echo "No cert file found"
   keytool -genkey -noprompt -storepass password -keypass password -keyalg RSA -alias tomcat -dname "CN=tomcat" -keystore /usr/share/tomcat.keystore
fi

catalina.sh run
