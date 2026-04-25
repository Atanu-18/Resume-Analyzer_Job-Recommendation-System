# from apify_client import ApifyClient
# import os 
# from dotenv import load_dotenv
# load_dotenv()

# apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))



# #fetch linkedin jobs based on search query and location
# def fetch_linkedin_jobs(search_query, location="india", rows=60):

#     run_input = {
#         "title": search_query,
#         "location": location,
#         "rows": rows,
#         "proxy": {
#             "useApifyProxy": True,
#             "apifyProxyGroups": ["RESIDENTIAL"],
#         },
#     }

#     run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)

#     jobs = list(
#         apify_client.dataset(run["defaultDatasetId"]).iterate_items()
#     )
#     return jobs



# #fetch naukri jobs based on search query and location
# def fetch_naukri_jobs(search_query, location="india", rows=60):

#     run_input = {
#         "keyword": search_query,
#         "maxJobs": rows,
#         "freshness": "all",
#         "sortBy": "relevance",
#         "experience": "all",
#     }

#     run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)

#     jobs = list(
#         apify_client.dataset(run["defaultDatasetId"]).iterate_items()
#     )

#     return jobs












from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))


# ---------------- LinkedIn Jobs ----------------
def fetch_linkedin_jobs(search_query, location="india", rows=60):

    try:
        run_input = {
            "title": search_query,
            "location": location,
            "rows": rows,
            "proxy": {
                "useApifyProxy": True,
                "apifyProxyGroups": ["RESIDENTIAL"],
            },
        }

        run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)

        jobs = list(
            apify_client.dataset(run["defaultDatasetId"]).iterate_items()
        )

        return jobs

    except Exception as e:
        print("LinkedIn fetch error:", e)
        return []   # 👈 SAFE FIX


# ---------------- Naukri Jobs ----------------
def fetch_naukri_jobs(search_query, location="india", rows=60):

    try:
        run_input = {
            "keyword": search_query,
            "maxJobs": rows,
            "freshness": "all",
            "sortBy": "relevance",
            "experience": "all",
        }

        run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)

        jobs = list(
            apify_client.dataset(run["defaultDatasetId"]).iterate_items()
        )

        return jobs

    except Exception as e:
        print("Naukri fetch error:", e)
        return []   # 👈 SAFE FIX