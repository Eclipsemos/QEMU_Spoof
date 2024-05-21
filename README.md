# QEMU-KVM BYPASS Virtualization Detection(EAC)
## Credits & Reference
- [Modify the configuration](https://docs.qq.com/aio/DWWRCalNHQmpBSVZD?p=pq8Zxa1F8viEIpvqozlmWQ)
- [Patch the QEMU](https://github.com/zhaodice/qemu-anti-detection)

## Generate the configuration
- Run sysinfo.py
- Enable the XML modification 
- Replace the [Template XML](./Template.md) with sysinfo.xml content

## KVM Setting
Inside the features
```XML
<kvm>
	<hidden state="on"/>
</kvm>
```
Customize the Hyper-V
```XML
<hyperv mode="custom">
		<relaxed state="on"/>
		<vapic state="on"/>
		<spinlocks state="on" retries="8191"/>
		<vpindex state="on"/>
		<runtime state="on"/>
		<synic state="on"/>
		<stimer state="on"/>
		<reset state="on"/>
		<vendor_id state="on" value="123456789123"/>
		<frequencies state="on"/>
	</hyperv>
```