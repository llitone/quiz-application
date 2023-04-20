using Tele2App.Model;

namespace Tele2App.ViewModel
{
    public class QuestionViewModel : BaseViewModel
    {
        public Question Question { get; set; }

        public QuestionViewModel(Question question)
        {
            Question = question;
        }
    }
}
