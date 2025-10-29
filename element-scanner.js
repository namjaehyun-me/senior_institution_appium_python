const { remote } = require('webdriverio');

async function scanElements() {
  const driver = await remote({
    port: 4723,
    capabilities: {
      platformName: 'Android',
      deviceName: 'Android Emulator',
      automationName: 'UiAutomator2',
      appPackage: 'com.teammapa.seniorcare.patient',
      appActivity: '.MainActivity'
    }
  });

  // 모든 요소 스캔
  const elements = await driver.$$('//*');
  
  for (let element of elements) {
    const text = await element.getText().catch(() => '');
    const resourceId = await element.getAttribute('resource-id').catch(() => '');
    const className = await element.getAttribute('class').catch(() => '');
    
    if (text || resourceId) {
      console.log({
        text,
        resourceId,
        className,
        selector: resourceId ? `~${resourceId}` : `text=${text}`
      });
    }
  }

  await driver.deleteSession();
}

scanElements();