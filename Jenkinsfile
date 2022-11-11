pipeline {

    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages{
        stage('Git-checkout'){
            steps{
                echo " Checking out git Repo"
                git branch: 'python', url: 'https://github.com/sabshock/DataGrokr.git'
            }
        }
        stage('build'){
        
            steps{
                echo 'building the app'
            }   
        }
        stage("test"){
            steps{
                 echo "Test"
            }
        }
        stage('deploy'){
        
            steps{
                bat 'docker build -t sab10/calculator_image .'
                
            }
        }
        
        stage('Push image') {
            withCredentials([usernamePassword( credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                def registry_url = "registry.hub.docker.com/"
                bat "docker login -u $USER -p $PASSWORD ${registry_url}"
                docker.withRegistry("http://${registry_url}", "dockerhub") {
            // Push your image now
            bat "docker push sab10/calculator_image"
        }
    }
}
    }
    
    post {
        always{
            bat 'docker logout'
        }
        success{
            echo 'calculator app docker image is successfully got deloyed to docker hub'
        }

    }
}
