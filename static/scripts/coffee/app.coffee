@App = Ember.Application.create()

App.Router.map () ->
  @resource 'index', path: '/'
  @resource 'projects'

App.ProjectsRoute = Ember.Route.extend
  model: () -> App.Project.find()


App.Store = DS.Store.extend
  revision: 12
  adapter: 'DS.DjangoRESTAdapter'



