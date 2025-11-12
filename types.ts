export interface AIModel {
  id: string
  name: string
  provider: string
  description?: string
}

export interface GeneratedCode {
  code: string
  model: string
  timestamp: number
}

export interface DeploymentResult {
  url: string
  appName: string
  success: boolean
}
