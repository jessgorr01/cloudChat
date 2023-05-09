pipeline {
    agent none 
    environment {
        docker_app = "main"
        GOCACHE = "/tmp"
        registry = "155.98.37.20"
        userid = "bd985346"
    }
    stages {
        stage('Build') {
            agent {
                kubernetes {
                    inheritFrom 'cloudChat'
                }
            }
            steps {
                container('cloudChat') {
                    // Create our project directory.
                    sh 'cd /webui'
                    sh 'npm install'
                    sh 'npm run build'
                     
                }
            }     
        }
        stage('Test') {
            agent {
                kubernetes {
                    inheritFrom 'cloudChat'
                }
            }
            steps {
                container('cloudChat') {                 
                    // Create our project directory.
                    sh 'cd /webui'
                    sh 'npm start deploy'
                }
            }
        }
        stage('Publish') {
            agent {
                kubernetes {
                    inheritFrom 'docker'
                }
            }
            steps{
                container('docker') {
                    sh 'docker login -u admin -p registry https://${registry}:443'
                    sh 'docker build -t ${registry}:443/cloudChat:$BUILD_NUMBER .'
                    sh 'docker push ${registry}:443/cloudChat:$BUILD_NUMBER'
                }
            }
        }
        stage ('Deploy') {
            agent {
                node {
                    label 'deploy'
                }
            }
            steps {
                sshagent(credentials: ['cloudlab']) {
                    sh "sed -i 's/REGISTRY/${registry}/g' cloudChat.yml"
                    sh "sed -i 's/DOCKER_APP/${docker_app}/g' cloudChat.yml"
                    sh "sed -i 's/BUILD_NUMBER/${BUILD_NUMBER}/g' cloudChat.yml"
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yml ${userid}@${registry}:~/'
                    sh 'ssh -o StrictHostKeyChecking=no ${userid}@${registry} kubectl apply -f /users/${userid}/deployment.yml'
                    sh 'ssh -o StrictHostKeyChecking=no ${userid}@${registry} kubectl apply -f /users/${userid}/cloudChat-service.yml'                                        
                }
            }
        }
    }
}
