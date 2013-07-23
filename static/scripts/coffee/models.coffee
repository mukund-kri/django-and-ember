App.Project = DS.Model.extend
  name: DS.attr 'string'
  tasks: DS.hasMany 'App.Task'

App.Task = DS.Model.extend
  name: DS.attr 'string'
  project: DS.belongsTo 'App.Project'



