using System.Net.Http.Json;
using Tele2App.Current;
using Tele2App.Model;
using static Android.Graphics.ColorSpace;

namespace Tele2App.Services
{
    public class LoginService
    {
        public async Task<bool> Login(LoginUserModel model)
        {
            try
            {
                HttpClient client = new HttpClient();
                string endpoint = $"http://127.0.0.1:1238/app/api/v1.0/users/{model.PhoneNumber}";

                HttpContent content = null;

                var response = await client.PostAsync(endpoint, content);
                if (!response.IsSuccessStatusCode)
                    return false;

                LoginUserModel result = await response.Content.ReadFromJsonAsync<LoginUserModel>();
                if (result.Password != model.Password)
                    return false;
                CurrentUser.Login(result);

                return true;
            }
            catch
            {
                return false;
            }
        }

        public async Task<bool> Login(string phoneNumber, string password)
        {
            try
            {
                HttpClient client = new HttpClient();
                string endpoint = $"http://127.0.0.1:1238/app/api/v1.0/users/{phoneNumber}";

                HttpContent content = null;

                var response = await client.PostAsync(endpoint, content);
                if (!response.IsSuccessStatusCode)
                    return false;

                LoginUserModel result = await response.Content.ReadFromJsonAsync<LoginUserModel>();
                if (result.Password != password)
                    return false;
                CurrentUser.Login(result);

                return true;
            }
            catch
            {
                return false;
            }
        }
    }
}
