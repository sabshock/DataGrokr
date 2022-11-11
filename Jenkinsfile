pipeline {

    agent any

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
                 echo "Testing"
                bat "py test_calc.py"
            }
        }
        stage('deploy'){
        
            steps{
                bat 'docker build -t sab10/calculator_image .'
                
            }
        }
        
        stage('Push image') {
            steps{
                echo "Logging into docker"
                withCredentials([usernamePassword( credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                    //def registry_url = "registry.hub.docker.com/"
                    bat "docker login -u $USER -p $PASSWORD "
                
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
