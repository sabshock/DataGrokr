pipeline {

    agent any

    stages{
        stage('build'){
        
            steps{
                echo 'building the app'
            }   
        }
        stage("test_branch"){
            when{
                expression {
                        BRANCH_NAME == "test"
                }   
            }
            steps{
                 echo "Test branch only get to print this msg"
            }
        }
        stage('test'){
        
            steps{
                echo 'testing the app'
            }
        }
        stage('deploy'){
        
            steps{
                echo 'deploy the app'
            }
        }
    }
}
