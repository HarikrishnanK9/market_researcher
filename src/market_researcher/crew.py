from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MarketResearcher():
    """MarketResearcher crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'],
            verbose=True
        )

    @agent
    def trend_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_reporter'],
            verbose=True
        )
    
    @task
    def trend_identification_task(self) -> Task:
        return Task(
            config=self.tasks_config['trend_identification_task'],
        )

    @task
    def trend_reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['trend_reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketResearcher crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
           
        )
