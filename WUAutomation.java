import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.awt.AWTException;
import java.awt.event.KeyEvent;

public class WUAutomation{
    Robot bot = new Robot();

    public static void main(String[] args) throws AWTException {
        new WUAutomation();
    }

    public WUAutomation() throws AWTException{
        bot.keyPress(KeyEvent.VK_META);
        bot.keyPress(KeyEvent.VK_SPACE);
        bot.keyRelease(KeyEvent.VK_META);
        bot.keyRelease(KeyEvent.VK_SPACE);

    }

    private void type(final int i){
        bot.delay(40);
        bot.keyPress(i);
        bot.keyRelease(i);
    }

    private void type(final String s)
    {
        final byte[] bytes = s.getBytes();
        for (final byte b : bytes)
        {
            int code = b;
            // keycode only handles [A-Z] (which is ASCII decimal [65-90])
            if (code > 96 && code < 123)
            {
                code = code - 32;
            }
            bot.delay(40);
            bot.keyPress(code);
            bot.keyRelease(code);
        }
    }
}