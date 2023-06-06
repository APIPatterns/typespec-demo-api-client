import asyncio
from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from demoproject.apiclient.gadget_client import GadgetClient
from demoproject.apiclient.models import gadget

async def main():
   # API requires no authentication, so use the anonymous
   # authentication provider
   auth_provider = AnonymousAuthenticationProvider()
   # Create request adapter using the HTTPX-based implementation
   request_adapter = HttpxRequestAdapter(auth_provider)

   request_adapter.base_url = "{Put URL Here}"
   client = GadgetClient(request_adapter)
   # GET /gadgets
   all_gadgets = await client.api.gadgets.get()
   print(f"Retrieved {len(all_gadgets.value)} gadgets.")

# Run main
asyncio.run(main())
