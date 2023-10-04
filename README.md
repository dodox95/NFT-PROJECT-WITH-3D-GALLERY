ArbmidasNFT Web Application
===========================

Description:
------------
The ArbmidasNFT is a Django based web application designed for the promotion, display, and handling of NFTs. It offers the ability for users to view collections, connect their wallets, check wallet connections, fetch NFT data, and more. The application also offers static file serving capabilities in development mode.

URL Routing (url.py):
---------------------
1. Admin Panel: /admin/
2. Home: /
3. Static Files: /staticfiles/<path>
4. NFT 3D Gallery: /gallery/
5. VIP Page: /pages/vip.html
6. Contact: /contact/
7. Connect Wallet: /connect-wallet/
8. Check Wallet Connection: /check-wallet-connection/
9. Staking: /staking/
10. Fetch NFT Data API: /api/fetch-nft-data/

Views (views.py):
-----------------
1. Home Page (main.html)
2. NFT 3D Gallery (index.html)
3. VIP Page (vip.html)
4. Contact Page (contact.html)
5. Connect Wallet API
6. Check Wallet Connection API
7. Staking Page (nft.html)
8. Fetch NFT Data API
9. 404 Error Handler (404.html)

Main Page (main.html):
----------------------
- Introduction to ArbmidasNFT collections.
- Instructions on how to get the NFTs.
- A showcase of the top artworks in 3D.
- Details about the team behind the ArbmidasNFT.
- Links to various sections of the site, including the gallery and contact page.

Requirements:
-------------
- Django Framework
- Requests Python Library for making API calls.

Setup & Run:
------------
1. Ensure Django and Requests library are installed.
2. Navigate to the project directory.
3. Run the Django server using the command: `python manage.py runserver`
4. Access the web application in your browser at http://localhost:8000/

Note:
-----
This application integrates with the Arbitrum API to fetch NFT data. Ensure you have a valid API key to make successful requests.

For further development or customization, please refer to the Django documentation and the comments within the provided code.
