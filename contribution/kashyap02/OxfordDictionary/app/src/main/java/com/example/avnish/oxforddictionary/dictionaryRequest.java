//package com.example.avnish.oxforddictionary;
//
//import android.content.Context;
//import android.os.AsyncTask;
//import android.util.Log;
//import android.widget.TextView;
//import android.widget.Toast;
//
//import org.json.JSONArray;
//import org.json.JSONException;
//import org.json.JSONObject;
//
//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.net.URL;
//
//import javax.net.ssl.HttpsURLConnection;
//
//public class dictionaryRequest extends AsyncTask<String,Integer,String> {
//
//    final String app_id = "09034f10";
//    final String app_key = "bd4a6fdac209224d238b9720d1d7fc42";
//    String Url;
//    Context context;
//    private TextView t1 ;
//
//    dictionaryRequest(Context context){
//        this.context = context;
//    }
//
//    @Override
//    protected String doInBackground(String... params) {
//        Url = params[0];
//        try {
//            URL url = new URL(Url);
//            HttpsURLConnection urlConnection = (HttpsURLConnection) url.openConnection();
//            urlConnection.setRequestProperty("Accept","application/json");
//            urlConnection.setRequestProperty("app_id",app_id);
//            urlConnection.setRequestProperty("app_key",app_key);
//
//            // read the output from the server
//            BufferedReader reader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
//            StringBuilder stringBuilder = new StringBuilder();
//
//            String line = null;
//            while ((line = reader.readLine()) != null) {
//                stringBuilder.append(line + "\n");
//            }
//
//            return stringBuilder.toString();
//
//        }
//        catch (Exception e) {
//            e.printStackTrace();
//            return e.toString();
//        }
//    }
//
//    @Override
//    protected void onPostExecute(String s) {
//        super.onPostExecute(s);
//        String def;
//        try{
//            JSONObject js = new JSONObject(s);
//            JSONArray results = js.getJSONArray("results");
//
//            JSONObject lEntries = results.getJSONObject(0);
//            JSONArray lsArray = lEntries.getJSONArray("lexical entries");
//
//            JSONObject entries = lsArray.getJSONObject(0);
//            JSONArray e = entries.getJSONArray("entries");
//
//            JSONObject json = e.getJSONObject(0);
//            JSONArray sensesArray = json.getJSONArray("senses");
//
//            JSONObject d = sensesArray.getJSONObject(0);
//            JSONArray de = d.getJSONArray("definitions");
//
//            def = de.getString(0);
//
//
//
//        }catch (JSONException e){
//            e.printStackTrace();
//        }
//    }
//
//
//}
