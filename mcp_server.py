from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

mcp = FastMCP("Job Recommender")


@mcp.tool()
def fetch_linkedin(listofkey: str):
    return fetch_linkedin_jobs(listofkey)


@mcp.tool()
def fetch_naukri(listofkey: str):
    return fetch_naukri_jobs(listofkey)


if __name__ == "__main__":
    mcp.run(transport="stdio")