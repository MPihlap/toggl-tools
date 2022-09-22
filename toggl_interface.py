from toggl import api
from toggl.utils import Config

class TogglInterface:
  def __init__(self) -> None:
    token = ""
    with open('token.txt') as f:
        token = f.read()

    self.config = Config.factory()  # Without None it will load the default config file
    self.config.api_token = token
    self.config.timezone = 'utc'  # Custom timezone

  def start_tracking(self, description, project_id=None, client=None):
    api.TimeEntry.start_and_save(
        config=self.config,
        description=description,
        project=project_id,
        client=client
    )

  def stop_tracking(self):
    current = api.TimeEntry.objects.current(config=self.config)
    if current is not None:
      current.stop_and_save()
