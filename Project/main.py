import java.io.FileWriter;
import java.io.IOException;

public class CSVWriter {

    public static void main(String[] args) {
        String[] rowData = {"Article link", "Website source", "Article type", "Article summary", "Article title", "Detailed article content", "Creation date", "Associated tags/hashtags", "Author's name", "Category"};

        // Sample data
        String[] articleData = {"https://example.com/article", "Example News", "2", "Summary of the article", "Title of the Article", "Detailed content of the article", "2024-04-06", "#blockchain #crypto", "John Doe", "Blockchain Technology"};

        try {
            FileWriter csvWriter = new FileWriter("blockchain_articles.csv");

            // Write header row
            for (String column : rowData) {
                csvWriter.append(column);
                csvWriter.append(",");
            }
            csvWriter.append("\n");

            // Write article data
            for (String data : articleData) {
                csvWriter.append(data);
                csvWriter.append(",");
            }
            csvWriter.append("\n");

            csvWriter.flush();
            csvWriter.close();

            System.out.println("Data has been written to blockchain_articles.csv");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

