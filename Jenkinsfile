pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "anithavalluri/python-app:latest"
        GIT_CREDENTIALS = "github-credentials"     // Jenkins credentials ID for GitHub
        DOCKER_CREDENTIALS = "anithavalluri-docker" // Jenkins credentials ID for Docker Hub
        KUBECONFIG_CREDENTIALS = "aws-creds"   // Jenkins credentials ID for kubeconfig (optional)
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                // 🔹 Secure Git checkout with credentials
                git branch: 'main', url: 'https://github.com/anithavalluri02/python1.git', credentialsId: "${GIT_CREDENTIALS}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh """
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r src/requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "No tests yet, add pytest later"'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing image to Docker Hub...'
                // 🔹 Secure Docker login using Jenkins credentials
                withDockerRegistry([credentialsId: "${DOCKER_CREDENTIALS}", url: 'https://index.docker.io/v1/']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

       stage('Create Kubernetes Container') {
    steps {
        echo 'Creating container in Kubernetes...'
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-creds']]) {
            sh '''
                aws eks update-kubeconfig --region ap-south-1 --name <your-cluster-name>
                kubectl run python-app \
                    --image=${DOCKER_IMAGE} \
                    --restart=Always \
                    --port=5000 \
                    --labels=app=python-app || echo "Container may already exist, continuing..."
            '''
        }
    }
}

stage('Deploy to Kubernetes') {
    steps {
        echo 'Deploying to Kubernetes...'
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-creds']]) {
            sh '''
                aws eks update-kubeconfig --region ap-south-1 --name <your-cluster-name>
                kubectl apply -f k8s/deployment.yaml
            '''
        }
    }
}


        stage('Expose Service in Kubernetes') {
            steps {
                echo 'Creating NodePort service for the app...'
                withCredentials([file(credentialsId: "${KUBECONFIG_CREDENTIALS}", variable: 'KUBECONFIG')]) {
                    sh '''
                        kubectl apply -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: python-app-service
spec:
  type: NodePort
  selector:
    app: python-app
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
      nodePort: 30500
EOF
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }
    }
}
