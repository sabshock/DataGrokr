pipeline {
    agent slave_1
    
    stages{
        stage ('Git-checkout') {
            steps{
                echo " Checking out git Repo"
                git branch: 'python', url: 'https://github.com/sabshock/DataGrokr.git'
            }
        }
        stage ('Test') {
            agent {
                docker { image 'python:3.8'}
            }
            steps{
                echo "Runing Unit test"    
                bat "py test_calc.py"
            }

        }

        stage ('docker image building') {
            
            steps{
                bat 'docker build -t sab10/calculator_image_by_dockeragent .'
                
            }
            steps ( 'docker image push') {
                echo "Logging into docker"
                withCredentials([usernamePassword( credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                    //def registry_url = "registry.hub.docker.com/"
                    bat "docker login -u $USER -p $PASSWORD "
                
                    // Push your image now
                    bat "docker push sab10/calculator_image_by_dockeragent"
                
                }

            }

        }
    }
    post {
        always {
            bat 'docker logout' 
        }
        success{
            echo 'calculator app docker image is successfully got deloyed to docker hub'
        }
    }

}