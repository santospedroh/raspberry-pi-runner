terraform {
  required_providers {
    gitlab = {
      source = "gitlabhq/gitlab"
      version = "3.8.0"
    }
  }
}

provider "gitlab" {
    token = "xxx"
}

resource "gitlab_project" "meu-projeto-gitlab" {
  name        = "meu-projeto-via-terraform"
  description = "Meu projeto IAC"
  visibility_level = "public"
}

output "projeto_name" {
    value = gitlab_project.meu-projeto-gitlab.name
}
