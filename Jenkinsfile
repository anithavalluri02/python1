pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "your-dockerhub-username/python-app:latest"
    }
    stages {
        stage('Checkout') {
            steps { git 'https://github.com/your-repo/python-app.git' }
        }
        stage('Install Dependencies') {
            steps { sh 'pip install -r src/requirements.txt' }
        }
        stage('Test') {
            steps { sh 'echo "No tests yet, add pytest later"' }
        }
        stage('Build Docker Image') {
            steps { sh "docker build -t $DOCKER_IMAGE ." }
        }
        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-creds', url: '']) {
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps { sh 'kubectl apply -f k8s/' }
        }
    }
}
