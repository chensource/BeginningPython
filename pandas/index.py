<?xml version = "1.0" encoding = "utf-8"?>
<!--
    有关如何配置 ASP.NET 应用程序的详细信息，请访问
    http: // go.microsoft.com / fwlink /?LinkId = 169433
    -->
<configuration >
    <configSections >
        <!-- For more information on Entity Framework configuration, visit http: // go.microsoft.com / fwlink /?LinkID = 237468 - ->
        <section name = "entityFramework" type = "System.Data.Entity.Internal.ConfigFile.EntityFrameworkSection, EntityFramework, Version=6.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" requirePermission = "false" / >
    < / configSections >
    <system.web >
        <compilation targetFramework = "4.5" / >
        <httpRuntime targetFramework = "4.5" / >
    < / system.web >
    <entityFramework >
        <defaultConnectionFactory type = "System.Data.Entity.Infrastructure.LocalDbConnectionFactory, EntityFramework" >
            <parameters >
                <parameter value = "mssqllocaldb" / >
            < / parameters >
        < / defaultConnectionFactory >
        <providers >
            <provider invariantName = "System.Data.SqlClient" type = "System.Data.Entity.SqlServer.SqlProviderServices, EntityFramework.SqlServer" / >
        < / providers >
    < / entityFramework >
    <connectionStrings >
    <add name = "NewEstateEntities" connectionString = "metadata=res://*/Models.NewEstate.csdl|res://*/Models.NewEstate.ssdl|res://*/Models.NewEstate.msl;provider=System.Data.SqlClient;provider connection string=&quot;data source=10.1.1.103;initial catalog=SoufangNewEstate_NN;persist security info=True;user id=CCDS_Temp;password=CCDS.2017;MultipleActiveResultSets=True;App=EntityFramework&quot;" providerName = "System.Data.EntityClient" / > < /connectionStrings >
        <system.webServer >
            <defaultDocument >
                <files >
                    <remove value = "default.aspx" / >
                    <remove value = "iisstart.htm" / >
                    <remove value = "index.html" / >
                    <remove value = "index.htm" / >
                    <remove value = "Default.asp" / >
                    <remove value = "Default.htm" / >
                    <add value = "index.aspx" / >
                < / files >
            < / defaultDocument >
        < / system.webServer >
< / configuration >
