# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from botcity.plugins.http import BotHttpPlugin

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Create a BotHttpPlugin instance
    base_url = "https://reqres.in/api"

    # Create routes to fetch users
    http = BotHttpPlugin(base_url + "/users?page=2")

    # Get the response
    print(http.get().json()['total'])
    print(http.get().json()['data'][0]['email'])

    # Login
    http = BotHttpPlugin(base_url + "/login")
    params = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }

    # Set the parameters
    http.set_params(params)
    print(http.post().text)


    # Register (DESAFIO)
    http = BotHttpPlugin(base_url + "/register")
    params = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    http.set_params(params)

    # Capture key 'token'
    print(http.post().json()['token'])



    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


if __name__ == '__main__':
    main()
