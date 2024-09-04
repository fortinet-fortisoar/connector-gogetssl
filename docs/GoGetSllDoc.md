
<h2>About the connector</h2>

<p>GOGETSSL offers SSL/TLS certificates and digital security solutions to secure websites, emails, and networks. With this connector, users can enhance security, streamline certificate management, and ensure trusted encryption for online communications</p>

<p>This document provides information about the GOGETSSL connector, which facilitates automated interactions, with a GOGETSSL server using FortiSOAR&trade; playbooks. Add the GOGETSSL connector as a step in FortiSOAR&trade; playbooks and perform automated operations with GOGETSSL.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-gogetssl</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of GOGETSSL server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the GOGETSSL server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>GOGETSSL</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Rest API endpoint URL of the GOGETSSL server to connect and perform automated operations.</td></tr>
<tr><td>API Key</td><td>Specify the API key to access the GOGETSSL Rest API endpoint to which you will connect and perform the automated operations.</td></tr>
<tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to <code>true</code>.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>You can use the following automated operations in playbooks and also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Domain Alternative</td><td>Retrieve information about alternative domain names associated with a specific SSL/TLS certificate.</td><td>get_domain_alternative <br/>Investigation</td></tr>
<tr><td>Get Domain Emails</td><td>Retrieve email addresses associated with a specific domain.</td><td>get_domain_emails <br/>Investigation</td></tr>
<tr><td>Get Geotrust Approval Emails</td><td>Retrieve email addresses associated with a domain specifically for GeoTrust SSL certificates.</td><td>get_domain_emails_for_geo_trust <br/>Investigation</td></tr>
<tr><td>Get Approver Emails</td><td>Retrieve an array of valid approver email addresses for specified domain.</td><td>get_domain_from_whois <br/>Investigation</td></tr>
<tr><td>Get All Products</td><td>Retrieve all products from GOGETSSL.</td><td>get_all_products <br/>Investigation</td></tr>
<tr><td>Get Product Details</td><td>Retrieving details of a specific product from GOGETSSL.</td><td>get_product_details <br/>Investigation</td></tr>
<tr><td>Get Orders Metadata</td><td>Retrieves common details about the order's status and associated metadata, helping you track and manage your SSL certificate orders.</td><td>get_orders_metadata <br/>Investigation</td></tr>
<tr><td>Get Orders Details</td><td>Retrieve comprehensive details about a specific SSL certificate order.</td><td>get_orders_details <br/>Investigation</td></tr>
<tr><td>Get All Orders Status</td><td>Retrieve the status of all SSL certificate orders associated with your account.</td><td>get_all_orders_status <br/>Investigation</td></tr>
<tr><td>Get Total Order Count</td><td>Retrieves the total number of SSL certificate orders associated with your account.</td><td>get_total_order_count <br/>Investigation</td></tr>
<tr><td>Generate CSR</td><td>Generate a Certificate Signing Request (CSR) based on the provided parameter values.</td><td>generate_csr <br/>Investigation</td></tr>
<tr><td>Validate CSR</td><td>Validate a Certificate Signing Request (CSR).</td><td>validate_csr <br/>Investigation</td></tr>
<tr><td>Decode CSR</td><td>Decode a Certificate Signing Request (CSR).</td><td>decode_csr <br/>Investigation</td></tr>
<tr><td>Add SSL Order</td><td>Add an SSL certificate order in GOGETSSL</td><td>add_ssl_order <br/>Investigation</td></tr>
<tr><td>Reissue SSL Order</td><td>Request a reissue of an existing SSL certificate.</td><td>reissue_ssl_order <br/>Investigation</td></tr>
<tr><td>Add SSL Renew Order</td><td>Renewal process for an existing SSL certificate.</td><td>add_ssl_renew_order <br/>Investigation</td></tr>
<tr><td>Add SSL SAN Order</td><td>Add an SSL certificate with Subject Alternative Names (SANs) to secure multiple domains or subdomains with a single certificate, ideal for Multi-Domain (MD) or Unified Communications (UCC) use.</td><td>add_ssl_san_order <br/>Investigation</td></tr>
<tr><td>Cancel Order</td><td>Cancel a previously placed SSL certificate order.</td><td>cancel_order <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Get Domain Alternative</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Provide Certificate Signing Request (CSR) to retrieve alternative domain names for your SSL/TLS certificate.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "validation": {
        "http": {
            "http": {
                "link": "",
                "filename": "",
                "content": ""
            }
        },
        "dns": {
            "dns": {
                "record": ""
            }
        }
    },
    "success": ""
}</pre>

<h3>operation: Get Domain Emails</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain</td><td>Specify the domain for which you want to retrieve associated email addresses.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "validation": {
        "http": {
            "http": {
                "link": "",
                "filename": "",
                "content": ""
            }
        },
        "dns": {
            "dns": {
                "record": ""
            }
        }
    },
    "success": ""
}</pre>

<h3>operation: Get Geotrust Approval Emails</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain</td><td>Specify the domain for which you want to retrieve email addresses. These email addresses are relevant for GeoTrust SSL certificate validation.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "GeotrustApprovalEmails": [],
    "success": ""
}</pre>

<h3>operation: Get Approver Emails</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain</td><td>Specify the domain to retrieve an array of valid approver email addresses.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "ComodoApprovalEmails": [],
    "GeotrustApprovalEmails": [],
    "success": ""
}</pre>

<h3>operation: Get All Products</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "products": [
        {
            "id": "",
            "name": "",
            "periods": [],
            "organization": "",
            "wildcard": "",
            "unlimited_servers": "",
            "is_multidomain": "",
            "wildcard_san_enabled": "",
            "multidomains_included": "",
            "single_san_included": "",
            "wildcard_san_included": "",
            "multidomains_maximum": "",
            "dcv_email": "",
            "dcv_dns": "",
            "dcv_http": "",
            "dcv_https": "",
            "recheck_caa": ""
        }
    ]
}</pre>

<h3>operation: Get Product Details</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Product ID</td><td>Specify the product ID for which you want to retrieve detailed information.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "products": [
        {
            "id": "",
            "name": "",
            "periods": [],
            "organization": "",
            "wildcard": "",
            "unlimited_servers": "",
            "is_multidomain": "",
            "wildcard_san_enabled": "",
            "multidomains_included": "",
            "single_san_included": "",
            "wildcard_san_included": "",
            "multidomains_maximum": "",
            "dcv_email": "",
            "dcv_dns": "",
            "dcv_http": "",
            "dcv_https": "",
            "recheck_caa": ""
        }
    ]
}</pre>

<h3>operation: Get Orders Metadata</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "order_id": "",
        "status": "",
        "valid_from": "",
        "valid_till": "",
        "common_name": ""
    }
]</pre>

<h3>operation: Get Orders Details</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Order ID</td><td>Specify the order ID for which you want to retrieve detailed information.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "order_id": "",
    "partner_order_id": "",
    "internal_id": "",
    "status": "",
    "status_description": "",
    "dcv_status": "",
    "product_id": "",
    "domain": "",
    "total_domains": "",
    "base_domain_count": "",
    "single_san_count": "",
    "wildcard_san_count": "",
    "approver_method": {
        "http": {
            "link": "",
            "filename": "",
            "content": ""
        }
    },
    "domains": "",
    "validity_period": "",
    "valid_from": "",
    "valid_till": "",
    "begin_date": "",
    "end_date": "",
    "csr_code": "",
    "crt_code": "",
    "ca_code": "",
    "server_count": "",
    "reissue": "",
    "reissue_now": "",
    "renew": "",
    "webserver_type": "",
    "upgrade": "",
    "approver_emails": "",
    "dcv_method": "",
    "admin_addressline1": "",
    "admin_addressline2": "",
    "admin_city": "",
    "admin_country": "",
    "admin_fax": "",
    "admin_phone": "",
    "admin_postalcode": "",
    "admin_region": "",
    "admin_email": "",
    "admin_firstname": "",
    "admin_lastname": "",
    "admin_organization": "",
    "admin_title": "",
    "org_addressline3": "",
    "org_city": "",
    "org_country": "",
    "org_fax": "",
    "org_phone": "",
    "org_postalcode": "",
    "org_region": "",
    "tech_organization": "",
    "tech_addressline1": "",
    "tech_addressline2": "",
    "tech_addressline3": "",
    "tech_city": "",
    "tech_country": "",
    "tech_fax": "",
    "tech_phone": "",
    "tech_postalcode": "",
    "tech_region": "",
    "tech_email": "",
    "tech_firstname": "",
    "tech_lastname": "",
    "tech_title": "",
    "ssl_price": "",
    "ssl_period": "",
    "manual_check": "",
    "pre_signing": "",
    "admin_msg": "",
    "free_ev_upgrade": "",
    "codesigning_inviteurl": "",
    "validation_description": "",
    "san": [
        {
            "san_name": "",
            "validation_method": "",
            "status": "",
            "status_description": "",
            "validation": {
                "http": {
                    "link": "",
                    "filename": "",
                    "content": ""
                }
            }
        }
    ],
    "success": true,
    "time_stamp": 1563873515
}</pre>

<h3>operation: Get All Orders Status</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>CIDs</td><td>Specify the CSV of CIDs for which you want to retrieve the status.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "order_id": "",
        "status": "",
        "expires": ""
    }
]</pre>

<h3>operation: Get Total Order Count</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "total_orders": "",
    "success": ""
}</pre>

<h3>operation: Generate CSR</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Common Name</td><td>Specify the fully qualified domain name (FQDN) for which the certificate is being requested.</td></tr>
<tr><td>Organization Name</td><td>Specify the name of your organization.</td></tr>
<tr><td>Department</td><td>Specify the division or department within your organization.</td></tr>
<tr><td>City</td><td>Specify the city where your organization is located.</td></tr>
<tr><td>State</td><td>Specify the state or province where your organization is based.</td></tr>
<tr><td>Country</td><td>Specify the two-letter country code of your organization’s location (e.g., US).</td></tr>
<tr><td>Email Address</td><td>Specify the email address of your organization.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "csr_code": "",
    "csr_key": "",
    "success": ""
}</pre>

<h3>operation: Validate CSR</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Certificate Signing Request (CSR)</td><td>Specify the CSR to be validated, provided in PEM format.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "csrResult": {
        "CN": "",
        "C": "",
        "OU": "",
        "O": "",
        "L": "",
        "S": "",
        "version": "",
        "Email": "",
        "dnsName(s)": "",
        "Key Size": "",
        "md5": "",
        "sha1": "",
        "sha256": "",
        "errorMessage": ""
    },
    "success": true
}</pre>

<h3>operation: Decode CSR</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Certificate Signing Request (CSR)</td><td>Specify the CSR to be decoded, provided in PEM format.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "csrResult": {
        "CN": "",
        "C": "",
        "OU": "",
        "O": "",
        "L": "",
        "S": "",
        "version": "",
        "Email": "",
        "dnsName(s)": "",
        "Key Size": "",
        "md5": "",
        "sha1": "",
        "sha256": "",
        "errorMessage": ""
    },
    "success": true
}</pre>

<h3>operation: Add SSL Order</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Product ID</td><td>Specify the unique identifier of the SSL product being ordered.</td></tr>
<tr><td>Certificate Signing Request (CSR)</td><td>Specify the Certificate Signing Request (CSR) in PEM format.</td></tr>
<tr><td>Server Count</td><td>Specify the number of servers or domains that an SSL certificate should cover.</td></tr>
<tr><td>Period</td><td>Specify the number of years for which the SSL certificate will be valid.</td></tr>
<tr><td>Web Server Type</td><td>Specifies the type of web server for which the SSL certificate is being ordered.</td></tr>
<tr><td>Additional Field</td><td>(Optional) Specify any additional fields required for the use case, and provide them in JSON format.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "product_id": "",
    "approver_method": {
        "http": {
            "link": "",
            "filename": "",
            "content": ""
        }
    },
    "order_id": "",
    "invoice_id": "",
    "order_status": "",
    "success": "",
    "san": [
        {
            "san_name": "",
            "validation_method": "",
            "status": 1,
            "status_description": "",
            "validation": {
                "http": {
                    "link": "",
                    "filename": "",
                    "content": ""
                }
            }
        }
    ],
    "order_amount": "",
    "currency": "",
    "tax": "",
    "tax_rate": ""
}</pre>

<h3>operation: Reissue SSL Order</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Order ID</td><td>Specify the ID of the order that uniquely identifies the SSL certificate associated with the order you wish to reissue.</td></tr>
<tr><td>Certificate Signing Request (CSR)</td><td>Specify the Certificate Signing Request (CSR) to create a new SSL certificate.</td></tr>
<tr><td>Web Server Type</td><td>Specify the type of web server for which the SSL certificate will be reissued.</td></tr>
<tr><td>DCV Method</td><td>Specify the method used to validate domain control as part of the SSL certificate reissue process</td></tr>
<tr><td>DNS Names</td><td>Specify the CSV list of domain names or subdomains that you want to include in the reissued SSL certificate.</td></tr>
<tr><td>Approver Emails</td><td>(Optional) Specifies the email addresses of the individuals who are authorized to approve the reissue of the SSL certificate.</td></tr>
<tr><td>Approver Email</td><td>(Optional) Specifies the email address of the individual who will receive the approval request for the SSL certificate reissue.</td></tr>
<tr><td>Signature Hash</td><td>(Optional) Specifies the hashing algorithm used to sign the Certificate Signing Request (CSR). </td></tr>
<tr><td>Additional Field</td><td>(Optional) Specify any additional fields required for the use case, and provide them in JSON format.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "product_id": "",
    "additional_domains_count": "",
    "additional_domains_price": "",
    "approvalEmails": [],
    "validation": {
        "dns": {
            "record": ""
        }
    },
    "order_id": "",
    "order_status": "",
    "success": ""
}</pre>

<h3>operation: Add SSL Renew Order</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Product ID</td><td>Specify the product ID for which the SSL certificate is being renewed.</td></tr>
<tr><td>Certificate Signing Request (CSR)</td><td>Specify the CSR (Certificate Signing Request) for the certificate you want to renew.</td></tr>
<tr><td>Server Count</td><td>Specify the number of servers or instances that will use the SSL certificate being renewed.</td></tr>
<tr><td>Period</td><td>Specifies the validity duration of the renewed SSL certificate.</td></tr>
<tr><td>Approver Emails</td><td>Specifies the email addresses of the individuals who are authorized to approve the renew of the SSL certificate.</td></tr>
<tr><td>Additional Field</td><td>(Optional) Specify any additional fields required for the use case, and provide them in JSON format.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "product_id": "",
    "approver_method": {
        "http": {
            "link": "",
            "filename": "",
            "content": ""
        }
    },
    "order_id": "",
    "invoice_id": "",
    "order_status": "",
    "success": "",
    "san": [
        {
            "san_name": "",
            "validation_method": "",
            "status": 1,
            "status_description": "",
            "validation": {
                "http": {
                    "link": "",
                    "filename": "",
                    "content": ""
                }
            }
        }
    ],
    "order_amount": "",
    "currency": "",
    "tax": "",
    "tax_rate": ""
}</pre>

<h3>operation: Add SSL SAN Order</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Order ID</td><td>Specify the order ID for which you want to add an SSL certificate with Subject Alternative Names (SANs).</td></tr>
<tr><td>Wildcard SAN Count</td><td>(Optional) Specify the number of wildcard SANs (e.g., *.example.com) to be included in the certificate.</td></tr>
<tr><td>Single SAN Count</td><td>(Optional) Specify the number of single SANs (e.g., www.example.com) to be included in the certificate.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Cancel Order</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Order ID</td><td>Specify the unique identifier of the SSL certificate order that you want to cancel.</td></tr>
<tr><td>Reason</td><td>(Optional) Specify the reason why the SSL certificate order is being canceled.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "message": "",
    "success": ""
}</pre>

<h2>Included playbooks</h2>

<p>The <code>Sample - GOGETSSL - 1.0.0</code> playbook collection comes bundled with the GOGETSSL connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the GOGETSSL connector.</p>

<ul>
<li>Add SSL Order</li>
<li>Add SSL Renew Order</li>
<li>Add SSL SAN Order</li>
<li>Cancel Order</li>
<li>Decode CSR</li>
<li>Generate CSR</li>
<li>Get All Orders Status</li>
<li>Get All Products</li>
<li>Get Domain Alternative</li>
<li>Get Domain Emails</li>
<li>Get Geotrust Approval Emails</li>
<li>Get Approver Emails</li>
<li>Get Orders Details</li>
<li>Get Orders Metadata</li>
<li>Get Product Details</li>
<li>Get Total Order Count</li>
<li>Reissue SSL Order</li>
<li>Validate CSR</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
