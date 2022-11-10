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
                        BRANCH_NAME == "python"
                }   
            }
            steps{
                 sh 'echo "inside test_branch stage"'
            }
        }
        stage('test'){
        
            steps{
                echo 'testing the app'
            }
        }
        }
    }
