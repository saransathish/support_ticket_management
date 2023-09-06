pipeline{
  agent any
    triggers{
      githubPush()
    }
    stages{
      stage("Checkout"){
        step{
          checkout scm
        }
      }
    }
    
  
}
