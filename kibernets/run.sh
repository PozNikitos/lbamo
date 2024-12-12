minikube start --insecure-registry="192.168.0.105:5061" --driver=docker

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

minikube service lb-api-service
