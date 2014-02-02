from base import BuildStep


class Ssh(BuildStep):
	def __init__(self, work_dir):
		self.work_dir = work_dir

	def BuildStepArgs(self):
		return {}

	def BuildStepDescription(self):
		return ()

	def BuildStep(self, repo, branch='HEAD'):
		return (0, "")