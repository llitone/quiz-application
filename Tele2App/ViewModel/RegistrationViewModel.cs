using Tele2App.Model;
using Tele2App.Services;
using Tele2App.Current;
using Tele2App.View;

namespace Tele2App.ViewModel
{
    public class RegistrationViewModel : BaseViewModel
    {
        private string _name;
        private int _age;
        private string _phoneNumber;
        private string _password;
        private string _repeatPassword;
        RegistrationService _service;

        public RegistrationViewModel()
        {
            _service = new RegistrationService();
        }

        public string Name
        {
            get { return _name; }
            set
            {
                _name = value;
                Notify(nameof(Name));
            }
        }

        public int Age
        {
            get { return _age; }
            set
            {
                _age = value;
                Notify(nameof(Age));
            }
        }

        public string PhoneNumber
        {
            get { return _phoneNumber; }
            set
            {
                _phoneNumber = value;
                Notify(nameof(PhoneNumber));
            }
        }

        public string Password
        {
            get { return _password; }
            set
            {
                _password = value;
                Notify(nameof(Password));
            }
        }

        public string RepeatPassword
        {
            get { return _repeatPassword; }
            set
            {
                _repeatPassword = value;
                Notify(nameof(RepeatPassword));
            }
        }

        public ButtonCommand Registration
        {
            get
            {
                return new ButtonCommand( async () =>
                {
                    if (_phoneNumber == null || _password == null || _name == null || _age == 0)
                        return;
                    if (_password != _repeatPassword)
                        return;
                    if (Connectivity.Current.NetworkAccess != NetworkAccess.Internet)
                    {
                        await Shell.Current.DisplayAlert("Ошибка", "Нет подключения к интернету, попробуйте позже", "ОК");
                        return;
                    }
                    RegistrationUserModel model = new()
                    {
                        Age = Age,
                        PhoneNumber = PhoneNumber,
                        Password = Encryptor.Encrypt(Password),
                        Name = Name,
                        Points = 0
                    };
                    bool isCorrect = await _service.Registration(model);
                    if (!isCorrect)
                        await Shell.Current.DisplayAlert("Ошибка", "Ошибка регистрации, попробуйте позже", "ОК");
                    else
                        await Shell.Current.GoToAsync(nameof(MainPage));
                });
            }
        }
    }
}
