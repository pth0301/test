//Import the datapusher class and utility functions
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            // Connect to the website
            Document doc = Jsoup.connect("https://www.blockchain.com/").get();

            // Extract elements by CSS selector
            Elements links = doc.select("a[href]");

            // Print out the extracted data
            for (Element link : links) {
                System.out.println(link.attr("href") + ": " + link.text());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
