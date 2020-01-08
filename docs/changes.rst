Change log
==========

Stable versions
~~~~~~~~~~~~~~~

Version 0.0.91 (January 08, 2020)
-------------------------------------

* refactor: Add typing to Loan object (e7e6af5)

Version 0.0.90 (January 05, 2020)
-------------------------------------

* build: Add python3 restriction to build (9be0af0)
* refactor: Remove python2 specific code in handlers module (30a54a8)
* Publish version 0.0.89 (0e1f2d7)
* refactor: Change args type in exception from list to tuple (a1cfb5e)
* Publish version 0.0.89 (137c2a3)
* doc: Update Readme (ed33146)

Version 0.0.89 (January 03, 2020)
-------------------------------------

* refactor: Change args type in exception from list to tuple (a1cfb5e)
* Publish version 0.0.89 (137c2a3)
* doc: Update Readme (ed33146)

Version 0.0.89 (January 02, 2020)
-------------------------------------

* doc: Update Readme (ed33146)

Version 0.0.89 (December 22, 2019)
-------------------------------------

* build: Update six dependency (8ce1d3f)

Version 0.0.88 (December 20, 2019)
-------------------------------------

* feat: Add methods for managing Client images (4040c0b)

Version 0.0.87 (December 08, 2019)
-------------------------------------

* build: Fix broken docker compose configuration (ed8b9ac)

Version 0.0.86 (December 07, 2019)
-------------------------------------

* build: Disable restarting of dockerr container (3c2e787)
* refactor: Add (hour,minute,second) to datetime conversions (fd43721)

Version 0.0.85 (November 26, 2019)
-------------------------------------

* test: Fix broken savings test (8f225b1)

Version 0.0.84 (November 18, 2019)
-------------------------------------

* feat: Add convenience methods to savings object (8bf3e3b)
* feat: Add savings object (273c9e9)
* build: Add util python file to simplify objects creation for API (0b8800a)

Version 0.0.83 (November 17, 2019)
-------------------------------------

* feat: Add methods for disbursing a loan application and undoing a loan disbursal (5181e8f)
* feat: Add methods for approving a loan application and undoing a loan application (592e85d)
* feat: Add method for deleting a loan application (1d55b2a)
* feat: Add loan application method to Loan object (5ee2bc5)
* feat: Add Note object (168cd79)

Version 0.0.82 (November 06, 2019)
-------------------------------------

* feat: Add method for fetching template to Loan object (f3e8454)

Version 0.0.81 (October 31, 2019)
-------------------------------------

* feat: Add convenience method to check if client is activated. (e7823fb)

Version 0.0.80 (October 30, 2019)
-------------------------------------

* feat: Add convenience method for checking if a loan is closed or not to Loan object (a63b0b6)

Version 0.0.79 (October 21, 2019)
-------------------------------------

* doc: Add documentation for Loan object (ec8a65a)
* refactor: Cleanup legacy pagination logic (7cae30d)

Version 0.0.78 (October 19, 2019)
-------------------------------------

* doc: Add documentation for Hook object (5524ce0)
* doc: Add documentation for Report object (44197ac)
* doc: Add document for the Document object (8079ac5)
* doc: Finish up client documentation (cf2e29e)
* doc: Finish documentation for datatable (2b653f0)

Version 0.0.77 (October 17, 2019)
-------------------------------------

* feat: Add documentation for DataTable object (b9936ee)

Version 0.0.76 (October 11, 2019)
-------------------------------------

* feat: Improve document upload metadata (b72284d)
* feat: Improve document upload metadata (f8afc7f)

Version 0.0.75 (October 11, 2019)
-------------------------------------

* feat: Add document type detection to document object (81a877e)

Version 0.0.74 (October 08, 2019)
-------------------------------------

* fix: Correct setting of Document object attributes (b915a2b)

Version 0.0.73 (October 07, 2019)
-------------------------------------

* feat: Handle `204` responses (d4ef8b3)

Version 0.0.72 (October 07, 2019)
-------------------------------------

* feat: Add method for deleting a client in pending state (2508928)

Version 0.0.71 (October 06, 2019)
-------------------------------------

* feat: Add convenience methods for Document and Client objects (888b742)
* feat: Add document object (a2ebedc)

Version 0.0.70 (October 01, 2019)
-------------------------------------

* feat: Add submitted on date field during client creation (8e9c678)

Version 0.0.69 (October 01, 2019)
-------------------------------------



Version  (October 01, 2019)
-------------------------------------



Version 0.0.68 (October 01, 2019)
-------------------------------------

* tests: Modify client creation test (91a1603)
* feat: Add middlename to client creation params (23ca1c8)

Version 0.0.67 (September 30, 2019)
-------------------------------------

* feat: Complete templates map (d5e8033)

Version 0.0.66 (September 28, 2019)
-------------------------------------

* feat: Add logic for retrieving templates (affa1dc)

Version 0.0.65 (September 28, 2019)
-------------------------------------

* feat: Add logic for updating client details (c3be05c)

Version 0.0.64 (September 27, 2019)
-------------------------------------

* refactor: change column names for datatable column object (76b8e66)

Version 0.0.63 (September 27, 2019)
-------------------------------------

* test: Correct python2 incompatibility (626270c)

Version 0.0.62 (September 26, 2019)
-------------------------------------

* feat: Add optional fields during client creation (a982d77)

Version 0.0.61 (September 25, 2019)
-------------------------------------

* feat: Add CRUD methods for datatable data (ce7c043)
* feat: Add CRUD methods for datatable (455e23b)
* feat: Add a datatable object (c1524ef)

Version 0.0.60 (September 11, 2019)
-------------------------------------

* feat: Add external id to loan object (10b7282)

Version 0.0.59 (July 29, 2019)
-------------------------------------

* fix: Correct bug in `get_loans_in_arrears` (7300c85)

Version 0.0.58 (July 27, 2019)
-------------------------------------

* fix: Correct bug in `get_loans_in_arrears` (599d5b7)

Version 0.0.57 (July 25, 2019)
-------------------------------------

* refactor: Update function for getting loans in arrears (40f6e6f)

Version 0.0.56 (July 15, 2019)
-------------------------------------

* feat: add 'User' object (8d85d8c)

Version 0.0.55 (July 04, 2019)
-------------------------------------

* feat: Add 'run' method to Report object (c740c22)

Version 0.0.54 (July 03, 2019)
-------------------------------------

* feat: Add flag to 'get_loan_in_arrears' method (bc81f12)

Version 0.0.53 (June 26, 2019)
-------------------------------------

* feat: Add convenience methods for Hook (23a0a67)

Version 0.0.52 (June 26, 2019)
-------------------------------------

* fix: Add Hook object (eb21497)

Version 0.0.51 (June 18, 2019)
-------------------------------------

* fix: Correct bug in Loan object (f08d6f7)

Version 0.0.50 (June 18, 2019)
-------------------------------------

* feat: Add convenience methods for Report object (eb1b4ef)
* feat: Add convenience methods for Report object (d0c4e7b)
* feat: Add Report object (20c782b)

Version 0.0.49 (June 13, 2019)
-------------------------------------

* feat: Add convenience (days_in_arrears) function to Loan object (c406f41)

Version 0.0.48 (June 06, 2019)
-------------------------------------

* feat: Add optional params for specific objects (Group, Client, Loan, LoanProduct) (e2b7628)

Version 0.0.47 (June 04, 2019)
-------------------------------------

* feat: Add LoanTransaction object (d0776a8)

Version 0.0.46 (May 30, 2019)
-------------------------------------

* feat: Add documentation fo `as_dict` method (683d559)
* feat: Add 'as_dict' method to convert fineract method to dictionary (d3172ae)

Version 0.0.45 (May 29, 2019)
-------------------------------------

* fix: Add name attribute to Group object (e859437)

Version 0.0.44 (May 28, 2019)
-------------------------------------

* feat: Integrate groups with client (6252f37)
* feat: Add group object (fe43877)

Version 0.0.43 (May 23, 2019)
-------------------------------------

* test: Correct client tests (8518d22)
* feat: Add method for creating a basic client (562329b)

Version 0.0.42 (May 15, 2019)
-------------------------------------

* test: Fix broken test for test_handlers (466c729)

Version 0.0.41 (May 15, 2019)
-------------------------------------

* fix: Correct issue in make_request (181f1c0)

Version 0.0.40 (May 14, 2019)
-------------------------------------

* feat: Add convenience method for getting loans in arrears. (4b1c35d)
* Publish version 0.0.39 (59f1133)

Version 0.0.39 (May 13, 2019)
-------------------------------------



Version 0.0.39 (May 13, 2019)
-------------------------------------

* feat: Add page selection to PaginatedList (0f77563)

Version 0.0.38 (May 11, 2019)
-------------------------------------

* doc: Add documentation for Client object (61e4843)

Version 0.0.37 (May 09, 2019)
-------------------------------------

* refactor: Replace PaginatedList implementation with new version (72d8c4a)
* feat: New pagination implementation (4b6422b)

Version 0.0.36 (May 08, 2019)
-------------------------------------

* doc: Add documentation for utilities (3c31af4)

Version 0.0.35 (May 06, 2019)
-------------------------------------

* doc: Add documentation for Fineract object (487a407)

Version 0.0.34-dev0 (April 27, 2019)
-------------------------------------

* doc: Update README (9d6018e)

Version 0.0.34 (April 25, 2019)
-------------------------------------

* feat: Add method for getting outstanding loans (685dc80)

Version 0.0.33 (April 20, 2019)
-------------------------------------

* fix: Correct issue in debug mode for PreparedRequest (8eca075)
* Update README.md (db503b8)

Version 0.0.32-dev1 (April 17, 2019)
-------------------------------------



Version 0.0.32-dev0 (April 17, 2019)
-------------------------------------

* refactor: Use PreparedRequests to enable debug mode (a8e83c4)

Version 0.0.32 (April 09, 2019)
-------------------------------------

* fix: This commit adds textwrap indent compatibility for  python2.7 (56c3834)

Version 0.0.31-dev0 (April 09, 2019)
-------------------------------------

* fix: This commit adds textwrap indent compatibility for  python2.7 (9f2287f)

Version 0.0.31 (April 09, 2019)
-------------------------------------

* fix: This commit adds textwrap indent compatibility for  python2.7 (c13cfce)

Version 0.0.30 (April 09, 2019)
-------------------------------------

* feat: Add debugging for response (14bb0f1)

Version 0.0.29 (April 08, 2019)
-------------------------------------

* build: Add fineract-instance cleanup (77c7ff9)

Version 0.0.28 (April 08, 2019)
-------------------------------------

* fix: Correct get_client_by_phone_no (559f9bb)

Version 0.0.27 (April 08, 2019)
-------------------------------------

* test: Add integration tests for fetching datatables data (472270c)

Version 0.0.26 (April 08, 2019)
-------------------------------------

* fix: Modify request_handle access in DataFineractObject (944fdc7)

Version 0.0.25 (April 07, 2019)
-------------------------------------

* test: Add integration tests for Staff object (9c332d7)
* test: Add integration tests for Office object (81ba0e0)
* test: Add integration tests for LoanProduct object (bfb7d70)
* test: Add integration tests for Role object (3f93aab)

Version 0.0.24-dev13 (April 06, 2019)
-------------------------------------

* fix: Correct ssl issues when making requests to the fineract instance (a33296b)
* fix: Correct ssl issues when making requests to the fineract instance (58aa48c)

Version 0.0.24-dev12 (April 06, 2019)
-------------------------------------

* fix: Correct ssl issues when making requests to the fineract instance (3c2816f)

Version 0.0.24-dev11 (April 06, 2019)
-------------------------------------

* fix: Correct ssl issues when making requests to the fineract instance (fb18430)

Version 0.0.24-dev10 (April 06, 2019)
-------------------------------------

* fix: Correct ssl issues when making requests to the fineract instance (fc25ba1)

Version 0.0.24-dev9 (April 06, 2019)
-------------------------------------

* build: Add python wait script (26828d5)

Version 0.0.24-dev8 (April 06, 2019)
-------------------------------------

* build: Add python wait script (d75a49f)

Version 0.0.24-dev7 (April 06, 2019)
-------------------------------------

* build: Add python wait script (d75a49f)

Version 0.0.24-dev7 (April 06, 2019)
-------------------------------------

* fix: integration tests (ccf20f2)

Version 0.0.24-dev6 (April 06, 2019)
-------------------------------------

* build: Add wait for endpoint script (fbcf50d)

Version 0.0.24-dev5 (April 06, 2019)
-------------------------------------

* build: Add wait for endpoint script (434e56b)

Version 0.0.24-dev4 (April 06, 2019)
-------------------------------------

* build: Add wait for endpoint script (a84cbc0)

Version 0.0.24-dev3 (April 06, 2019)
-------------------------------------

* build: Add wait for endpoint script (f8bb335)

Version 0.0.24-dev2 (April 06, 2019)
-------------------------------------

* build: Add fineract integration tests (56be07e)

Version 0.0.24-dev1 (April 06, 2019)
-------------------------------------

* build: Add fineract integration tests (7b50f44)

Version 0.0.24-dev0 (April 06, 2019)
-------------------------------------

* build: Add fineract integration tests (71ff2cc)
* fix: Correct issues with Client operations (7ef0a40)
* fix: Correct issue when fetching client by phone (cbb8442)

Version 0.0.24 (April 05, 2019)
-------------------------------------

* fix: Add exception handling in make_requests (26d590c)

Version 0.0.23 (April 04, 2019)
-------------------------------------

* fix: Correct issue when getting single client by phone no (ff170f4)

Version 0.0.22 (April 04, 2019)
-------------------------------------

* feat: Add classmethod to Client object to get a client by phone no (aa3665d)

Version 0.0.21 (April 01, 2019)
-------------------------------------

* feat: Add LoanRepaymentSchedule object (e584f4c)
* style: Correct undo_withdrawal typo in method name. (1303301)

Version 0.0.20 (March 30, 2019)
-------------------------------------

* feat: Added convenience methods for a client (e125b92)

Version 0.0.19-dev8 (March 28, 2019)
-------------------------------------

* doc: Add changes to documenations (ce4de68)

Version 0.0.19-dev7 (March 27, 2019)
-------------------------------------

* fix: Correct setup.py (3b145e4)

Version 0.0.19-dev6 (March 27, 2019)
-------------------------------------

* fix: Correct setup.py (31c9369)

Version 0.0.19-dev5 (March 27, 2019)
-------------------------------------

* docs: Configure documentation file (3599c9b)

Version 0.0.19-dev4 (March 27, 2019)
-------------------------------------

* docs: Configure documentation file (9bbb5bb)

Version 0.0.19-dev3 (March 27, 2019)
-------------------------------------

* docs: Configure documentation file (c549ee0)

Version 0.0.19-dev2 (March 27, 2019)
-------------------------------------

* Update README.md (4870ede)

Version 0.0.19-dev1 (March 27, 2019)
-------------------------------------



Version 0.0.19-dev0 (March 27, 2019)
-------------------------------------

* docs: (eee6078)
