# BigData_TD1

This API allows you to make a ToDo list using and to deploy it
using a dockerImage. 

In order to implement this you will need to install kubctl and minikube.

Once the previous steps completed you can run these commands to setup and scale your Pods:

`minikube start`

`kubectl create deployment mytodolist --image=adem0rahal/myapi`

`kubectl expose deployment mytodolist --type=NodePort --port=5000`

You can scale it using :

`kubectl scale deployment mytodolist --replicas=30`

Then test it using :

`minikube service mytodolist`

Enjoy :)
