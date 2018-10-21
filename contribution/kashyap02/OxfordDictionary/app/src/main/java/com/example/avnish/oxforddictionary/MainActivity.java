package com.example.avnish.oxforddictionary;

import android.media.Image;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toolbar;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;

public class MainActivity extends AppCompatActivity {
    private EditText inputText;
    private ImageView searchButton;
    private TextView searchedWord;
    private ImageView speak;
    private TextView grammar;
    private TextView outputText;
    String word;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        inputText = (EditText)findViewById(R.id.inputText);
        searchButton = (ImageView)findViewById(R.id.search_button);
        searchedWord = (TextView)findViewById(R.id.searched_word);
        speak = (ImageView)findViewById(R.id.pronounce);
        grammar = (TextView)findViewById(R.id.grammar);
        outputText = (TextView)findViewById(R.id.outputText);

        searchButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                searchedWord.setText(inputText.getText().toString());
                word = inputText.getText().toString();
                speak.setImageResource(R.drawable.speaker);
                new CallbackTask().execute(dictionaryEntries(word));
            }
        });
    }


    private String dictionaryEntries(String wordToBeSearched) {
        final String language = "en";
        final String word = wordToBeSearched;
        final String word_id = word.toLowerCase();//word id is case sensitive and lowercase is required
        return "https://od-api.oxforddictionaries.com:443/api/v1/entries/" + language + "/" + word_id;
    }

    private class CallbackTask extends AsyncTask<String, Integer, String> {

        @Override
        protected String doInBackground(String... params) {
            final String app_id = "09034f10";
            final String app_key = "bd4a6fdac209224d238b9720d1d7fc42";
            try {
                URL url = new URL(params[0]);
                HttpsURLConnection urlConnection = (HttpsURLConnection) url.openConnection();
                urlConnection.setRequestProperty("Accept", "application/json");
                urlConnection.setRequestProperty("app_id", app_id);
                urlConnection.setRequestProperty("app_key", app_key);

                // read the output from the server
                BufferedReader reader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                StringBuilder stringBuilder = new StringBuilder();

                String line = null;
                while ((line = reader.readLine()) != null) {
                    stringBuilder.append(line + "\n");
                }

                return stringBuilder.toString();

            } catch (Exception e) {
                e.printStackTrace();
                return e.toString();
            }
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);
            String def = "";
            try{
                JSONObject js = new JSONObject(s);
                JSONArray results = js.getJSONArray("results");

                JSONObject lEntries = results.getJSONObject(0);
                JSONArray lsArray = lEntries.getJSONArray("lexicalEntries");

                JSONObject entries = lsArray.getJSONObject(0);
                JSONArray e = entries.getJSONArray("entries");

                JSONObject json = e.getJSONObject(0);
                JSONArray sensesArray = json.getJSONArray("senses");

                JSONObject d = sensesArray.getJSONObject(0);
                JSONArray de = d.getJSONArray("definitions");

                def = de.getString(0);

                outputText.setText(def);
            }catch (JSONException e){
                e.printStackTrace();
            }
        }
    }
}
