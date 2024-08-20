from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker # type: ignore
from rasa_sdk.executor import CollectingDispatcher # type: ignore
from gql import Client, gql # type: ignore
from gql.transport.requests import RequestsHTTPTransport # type: ignore

class QueryNeo4jPatients(Action):
    def name(self) -> Text:
        return "action_query_neo4j_Patients"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = gql('''
            query Patients {
                patients {
                    patient_ID
                    name
                    age
                    medical_history
                }
            }
        ''')

        transport = RequestsHTTPTransport(
            url='http://localhost:4000/graphql',
            use_json=True,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        try:
            result = client.execute(query)
            patients = result.get('patients', [])
            if patients:
                patients_list = "\n".join([f"- {patient['patient_ID']}, {patient['name']}, {patient['age']}, medical_history: {patient['medical_history']}" for patient in patients])
                dispatcher.utter_message(text=f"Here are the list of patients:\n{patients_list}")
            else:
                dispatcher.utter_message(text="No patients found.")
        except Exception as e:
            dispatcher.utter_message(text="Failed to query patients from Neo4j.")
            print(e)

        return []

class QueryNeo4jHealthcare_Providers(Action):
    def name(self) -> Text:
        return "action_query_neo4j_Healthcare_Providers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = gql('''
            query healthcareProviders {
                healthcareProviders {
                    provider_ID
                    name
                    specialization
                    location
                }
            }
        ''')

        transport = RequestsHTTPTransport(
            url='http://localhost:4000/graphql',
            use_json=True,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        try:
            result = client.execute(query)
            healthcareProviders = result.get('healthcareProviders', [])
            if healthcareProviders:
                healthcareProviders_list = "\n".join([f"- {provider['provider_ID']}, {provider['specialization']}, {provider['location']}" for provider in healthcareProviders])
                dispatcher.utter_message(text=f"Here are the list of healthcare providers:\n{healthcareProviders_list}")
            else:
                dispatcher.utter_message(text="No healthcare providers found.")
        except Exception as e:
            dispatcher.utter_message(text="Failed to query healthcare providers from Neo4j.")
            print(e)

        return []

class QueryNeo4jMedical_Services(Action):
    def name(self) -> Text:
        return "action_query_neo4j_Medical_Services"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = gql('''
            query medicalServices {
                medicalServices {
                    service_ID
                    name
                    description
                    associated_costs
                }
            }
        ''')

        transport = RequestsHTTPTransport(
            url='http://localhost:4000/graphql',
            use_json=True,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        try:
            result = client.execute(query)
            medicalServices = result.get('medicalServices', [])
            if medicalServices:
                medicalServices_list = "\n".join([f"- {service['service_ID']}, {service['description']}, {service['associated_costs']}, {service['name']}" for service in medicalServices])
                dispatcher.utter_message(text=f"Here are the list of medical services:\n{medicalServices_list}")
            else:
                dispatcher.utter_message(text="No medical services found.")
        except Exception as e:
            dispatcher.utter_message(text="Failed to query medical services from Neo4j.")
            print(e)

        return []
