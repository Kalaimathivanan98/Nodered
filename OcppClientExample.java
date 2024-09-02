import eu.chargetime.ocpp.OcppClient;
import eu.chargetime.ocpp.OcppVersion;
import eu.chargetime.ocpp.model.core.AuthorizeRequest;
import eu.chargetime.ocpp.model.core.AuthorizeResponse;

public class OcppClientExample {

    public static void main(String[] args) {
        // Replace with your OCPP server URL and Charge Point ID
        String serverUrl = "ws://ocpp.example.com:8080/ocpp"; // Use your actual server URL
        String chargePointId = "CP001"; // Your Charge Point ID

        // Create an OCPP client instance
        OcppClient client = new OcppClient(OcppVersion.V201, serverUrl, chargePointId);

        // Connect to the OCPP server
        client.connect();

        // Create and send an Authorize request
        AuthorizeRequest request = new AuthorizeRequest("user123");
        client.send(request);

        // Receive and handle the Authorize response
        AuthorizeResponse response = client.receive(AuthorizeResponse.class);
        System.out.println("Authorize response: " + response.getStatus());

        // Disconnect from the server
        client.disconnect();
    }
}
