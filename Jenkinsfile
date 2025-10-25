pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "anithavalluri/python-app:latest"
    }
    stage('Checkout') {
    steps {
        git branch: 'main', url: 'https://github.com/anithavalluri02/python1.git'
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
                withDockerRegistry([credentialsId: 'dockerhub-cred', url: '']) {
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps { sh 'kubectl apply -f k8s/' }
        }
    }
}
